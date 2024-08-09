(defn greet [name]
  ;; Parameters
  ;; name: a string representing the name of a person

  ;; Description
  ;; returns "Hello " + name as a string

  (format "Hello %s" name)
) ;; End of greet


(defn fib [n]
        ;; Parameters
	;; n: an integer for the value of fibonacci to return

	;; Description
	;; Recursively return nth fibonacci number

        (if (<= n 1)
                n
                (+ (fib (- n 1)) (fib (- n 2)))
	)
) ;; End of fib()


;; Test Functions


(format "Fibonacci(10) = %d" (fib 10))
;; Returns "Fibonacci(10) = 55"

(format "greet 'Kieran' = %s" (greet "Kieran"))
;; Returns "greet("Kieran") = Hello kieran"