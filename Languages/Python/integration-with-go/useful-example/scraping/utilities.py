import os
from platform import platform
from dataclasses import dataclass
from ctypes import cdll, Structure, c_char_p, c_int, POINTER

# import library
if platform().lower().startswith("windows"):
    lib = cdll.LoadLibrary(os.path.join(os.path.dirname(os.path.realpath(__file__)), "go", "lib.dll"))
else:
    lib = cdll.LoadLibrary(os.path.join(os.path.dirname(os.path.realpath(__file__)), "go", "lib.so")) 

class _CSite(Structure):
    """The C compatible Site structure, DO NOT USE DIRECTLY, use Site instead"""
    _fields_ = [
        ("url", c_char_p),
        ("domain", c_char_p),
        ("server", c_char_p),
        ("protocol", c_char_p),
        ("contentType", c_char_p),
        ("body", c_char_p),
        ("port", c_int),
    ]

# Set function return/arg types
lib.parse_urls.argtypes = [POINTER(c_char_p), c_int]
lib.parse_urls.restype = POINTER(_CSite)

lib.scrape_single_url.argtypes = [c_char_p]
lib.scrape_single_url.restype = POINTER(_CSite)

lib.free_site.argtypes = [POINTER(_CSite)]
lib.free_sites.argtypes = [POINTER(_CSite), c_int]

@dataclass
class Site:
    url:str         # the raw URL
    domain:str      # The domain the URL is hosted at
    server:str      # The value of the server header
    protocol:str    # The protocl of the site (http or https)
    contentType:str # The content type of the body (i.e. "text/html")
    body:str        # The body of the url
    port:int        # The port the url is on
    
    @classmethod
    def from_str(cls:'Site', url:str) -> 'Site':
        pointer = lib.scrape_single_url(url.encode("utf-8"))
        if not pointer:
            raise ValueError(f"Failed to scrape: {url}")
        try:
            data = pointer.contents
            result = cls(
                url=data.url.decode(errors="replace"),
                domain=data.domain.decode(errors="replace"),
                server=data.server.decode(errors="replace"),
                protocol=data.protocol.decode(errors="replace"),
                contentType=data.contentType.decode(errors="replace"),
                body=data.body.decode(errors="replace"),
                port=data.port,
            )
        except Exception as e:
            from traceback import format_tb
            tb = "".join(format_tb(e))
            print(f"Error while fetching: \n\t{tb}")
            if not pointer:
                raise ValueError(f"Failed to scrape: {url}")
            lib.free_site(pointer)
        return result

    @classmethod
    def from_urls(cls:'Site', urls:list[str]) -> list['Site']:
        count = len(urls)
        encoded = [c_char_p(url.encode("utf-8")) for url in urls]
        
        # Create a C array of char* (aka **char)
        array_type = c_char_p * count
        
        url_array = array_type(*encoded)
        print("Parsing URL's")
        pointer = lib.parse_urls(url_array, count)
        if not pointer:
            raise ValueError("Failed to parse URLs")

        results = []
        for i in range(count):
            site_ptr = pointer[i]
            data = site_ptr
            try:
                results.append(cls(
                    url=data.url.decode(errors="replace"),
                    domain=data.domain.decode(errors="replace"),
                    server=data.server.decode(errors="replace"),
                    protocol=data.protocol.decode(errors="replace"),
                    contentType=data.contentType.decode(errors="replace"),
                    body=data.body.decode(errors="replace"),
                    port=data.port
                ))
            except AttributeError:
                continue # No data
        cls.free_sites(pointer[0],count )
        return results

    @staticmethod
    def free_sites(array_pointer: _CSite, count:int):
        if not array_pointer:
            return
        lib.free_sites(array_pointer, count)