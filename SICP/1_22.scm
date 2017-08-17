#lang sicp

(define (square x) (* x x)) ; helpers
(define (even? x) (= (remainder x 2) 0))

(define (smallest-divisor n) ; smallest divisor
  (find-divisor n 2))
(define (find-divisor n test-divisor)
  (cond ((> (square test-divisor) n) n)
        ((divides? test-divisor n) test-divisor)
        (else (find-divisor n (+ test-divisor 1)))))
(define (divides? a b)
  (= (remainder b a) 0))

(define (prime? n) ; test for primality O(sqrt(n))
  (= n (smallest-divisor n)))

(define (timed-prime-test n)
  (start-prime-test n (runtime)))
(define (start-prime-test n start-time)
  (define (report-prime elapsed-time)
    (newline)
    (display n)
    (display " *** ")
    (display elapsed-time))
  (if (prime? n)
      (report-prime (- (runtime) start-time))))

(define (search-for-primes begin end)
  (define (search current)
    (cond ((even? current) (search (inc current)))         
          ((= current end) (timed-prime-test current))
          (else (timed-prime-test current)
                (if (not (= (+ current 1) end))
                    (search (inc current))))))
  (search begin))

(display "The three smallest prime numbers greater than 1,000:")
(search-for-primes 1000 1019)
(newline)

(display "The three smallest prime numbers greater than 10,000:")
(search-for-primes 10000 10037)
(newline)

(display "The three smallest prime numbers greater than 100,000:")
(search-for-primes 100000 100043)
(newline)

(display "The three smallest prime numbers greater than 1,000,000:")
(search-for-primes 1000000 1000037)
(newline)