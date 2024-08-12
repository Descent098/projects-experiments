
a = 1:10 # Creates an iterator

for num in 1:10
    println(num)
end


collect(a) # Returns a list of 1-10

using Printf # import package to run

@printf "Here is the list version of the iterator %s" collect(a)



