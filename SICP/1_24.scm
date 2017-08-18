#lang sicp
(#%require (only racket random)) ; import racket random function

(define (square x) (* x x)) ; helpers
(define (even? x) (= (remainder x 2) 0))
(define (next x)
  (if (= x 2)
      3
      (+ x 2)))

(define (expmod base exp m) ; exponential of a number modulo another
  (cond ((= exp 0) 1)
        ((even? exp)
         (remainder (square (expmod base (/ exp 2) m))
                    m))
        (else
         (remainder (* base (expmod base (- exp 1) m))
                    m))))

(define (fermat-test n) ; fermat's little theorem test
  (define (try-it a)
    (= (expmod a n n) a))
  (try-it (+ 1 (random (- n 1)))))

(define (fast-prime? n times) ; perform fermat's test on number 'n', 'times' times.
  (cond ((= times 0) #t)
        ((fermat-test n) (fast-prime? n (- times 1)))
        (else #f)))

(define (timed-prime-test n)
  (start-prime-test n (runtime)))
(define (start-prime-test n start-time)
  (define (report-prime elapsed-time)
    (newline)
    (display n)
    (display " *** ")
    (display elapsed-time))
  (if (fast-prime? n 12)
      (report-prime (- (runtime) start-time))))

(timed-prime-test 1999)
(timed-prime-test 1000000007)

;Time grows faster than log(n),
;probably due to the accumulation of primitive processes becoming noticeable as n grows.