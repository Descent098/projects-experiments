//! By convention, main.zig is where your main function lives in the case that
//! you are building an executable. If you are making a library, the convention
//! is to delete this file and start with root.zig instead.
const std = @import("std");
const print = std.debug.print;
const net = std.net;

pub fn main() !void {
    const addr = net.Address.resolveIp("127.0.0.1", 9090) catch |err| {
        print("An error occured while resolving the IP address: {}\n", .{err});
        return;
    };

    while (true) {
        var server = try addr.listen(.{});
        defer server.stream.close();
        var client = try server.accept();
        defer client.stream.close();
        std.debug.print("Client accepted on {d}.\n", .{addr.getPort()});
        try handleConnection(&client);
    }

    // Prints to stderr (it's a shortcut based on `std.io.getStdErr()`)
}

pub fn handleConnection(conn: *net.Server.Connection) !void {
    var stream = conn.stream;
    print("Sending response to {any}", .{conn.address});
    const response: []const u8 = "200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n<h1>Hello world</h1>";
    try stream.writeAll(response);
}

test "simple test" {
    var list = std.ArrayList(i32).init(std.testing.allocator);
    defer list.deinit(); // Try commenting this out and see if zig detects the memory leak!
    try list.append(42);
    try std.testing.expectEqual(@as(i32, 42), list.pop());
}

test "use other module" {
    try std.testing.expectEqual(@as(i32, 150), lib.add(100, 50));
}

test "fuzz example" {
    const global = struct {
        fn testOne(input: []const u8) anyerror!void {
            // Try passing `--fuzz` to `zig build test` and see if it manages to fail this test case!
            try std.testing.expect(!std.mem.eql(u8, "canyoufindme", input));
        }
    };
    try std.testing.fuzz(global.testOne, .{});
}

/// This imports the separate module containing `root.zig`. Take a look in `build.zig` for details.
const lib = @import("networking_lib");
