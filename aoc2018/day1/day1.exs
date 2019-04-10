case File.read("day1_inputs") do
    {:ok, contents} -> contents |> String.split("\n") |> Enum.map(&String.to_integer/1) |> Enum.reduce(fn(x, acc) -> x + acc end)
    {:error, reason} -> IO.puts("error: #{reason}")
end
