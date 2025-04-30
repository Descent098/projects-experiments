# An in-dveleopment no-code platform
from typing import List
from uuid import uuid4, UUID
from dataclasses import dataclass


@dataclass
class Pipe:
    """Datastructure that manages tranmission and recieving between Components"""
    type: str # inbound or outbound
    callback: callable

@dataclass
class Component:
    """An individual compoenent that is an atomized unit of data and templating,
    with associated pipes for ingress and egress
    """
    id : UUID
    inbound: List[Pipe]
    outbound: List[Pipe]
    view: str # template
    data: dict

task = Component(uuid4(), [],[],"<div><h2>{{self.data.description}}</h2><p>{{self.data.due}}</p></div>", {"description": "", "due": "", "completed":False})



@dataclass
class API:
    slug: str
    inbound: List[Pipe]
    outbound: List[Pipe]


@dataclass
class Page:
    components: List[Component]

@dataclass
class Application:
    title: str
    APIs: List[API]