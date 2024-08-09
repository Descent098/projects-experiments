defmodule Greeter do
  def greet(name) do
    IO.puts "Hello #{name}"
  end
end

# Example running function
if function_exported?(Greeter, :print_with_index, 1) do
  Greeter.greet("Kieran")
end


defmodule ListPrinter do
  def print_with_index(list) when is_list(list) do
    list
    |> Enum.with_index()
    |> Enum.each(fn {item, index} ->
      IO.puts("#{index}: #{item}")
    end)
  end
end

# Example running function
if function_exported?(ListPrinter, :print_with_index, 1) do
  sample_list = ["apple", "banana", "cherry"]
  ListPrinter.print_with_index(sample_list)
end