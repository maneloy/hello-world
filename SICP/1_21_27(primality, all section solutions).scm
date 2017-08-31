#lang scheme

;; code corresponding to section 1.2.6 from SICP
;; solutions not by me, simply storing for later use

(define (slow-expmod base exp m)
  (remainder (fast-expt base exp) m))
(define (fast-expt b n)
  (cond ((= n 0) 1)
        ((even? n) (square (fast-expt b (/ n 2))))
        (else (* b (fast-expt b (- n 1))))))

(define (smallest-divisor n)
  (find-divisor n 2))
(define (find-divisor n test-divisor)
  (cond ((> (square test-divisor) n) n)
        ((divides? test-divisor n) test-divisor)
        (else (find-divisor n (next test-divisor)))))
(define (square x) (* x x))
(define (divides? a b)
  (= (remainder b a) 0))
(define (next x)
  (if (= x 2)
      3
      (+ x 2)))

(define (prime? n)                  ;; T(n) = O(sqrt n)
  (= (smallest-divisor n) n)) 

(define (expmod base exp m)
  (cond ((= exp 0) 1)
        ((even? exp)
         (remainder (square (expmod base (/ exp 2) m))
                    m))
        (else
         (remainder (* base (expmod base (- exp 1) m))
                    m))))
(define (even? n)
  (= (remainder n 2) 0))

(define (fermat-test n)
  (define (try-it a)
    (= (expmod a n n) a))
  (try-it (+ 1 (random (- n 1)))))

(define (fast-prime? n times)       ;; T(n) = O(log n)
  (cond ((= times 0) true)
        ((fermat-test n) (fast-prime? n (- times 1)))
        (else false)))

(define (runtime) (current-milliseconds))
(define (timed-prime-test n)
  (start-prime-test n (runtime)))
(define (start-prime-test n start-time)
  (cond ((fast-prime? n 100)
         (newline)
         (display n)
         (report-prime (- (runtime) start-time)))))
(define (report-prime elapsed-time)
  (display " *** ")
  (display elapsed-time))

(define (search-for-primes first last)          ;; SEARCH FOR PRIMES
  (define (search-iter cur last)
    (cond ((<= cur last) (timed-prime-test cur)
                         (search-iter (+ cur 2) last))))
  (search-iter (if (even? first) (+ first 1) first)
               (if (even? last) (- last 1) last)))

(define (full-fermat-test? n) ;; Will return True for primes and Carmichael numbers.
  (define (try-it a n)
    (cond ((and (= (expmod a n n) a) (< a n)) (try-it (+ a 1) n))
          ((= a n) true)
          (else false)))
  (try-it 1 n))

;; MILLER-RABIN TEST (Carmichaels can't fool it)
(define (miller-rabin n)
  (miller-rabin-test (- n 1) n))
(define (miller-rabin-test a n)
  (cond ((= a 0) true)
        ((= (expmod a (- n 1) n) 1) (miller-rabin-test (- a 1) n))
        (else false)))
(define (mr-expmod base exp m)
  (cond ((= exp 0) 1)
        ((even? exp)
         (let ((x (expmod base (/ exp 2) m)))
         (if (non-trivial-sqrt? x m) 0 (remainder (square x) m))))
        (else (remainder (* base (expmod base (- exp 1) m)) m))))
(define (non-trivial-sqrt? n m)
  (cond ((= n 1) false)
        ((= n (- m 1)) false)
        (else (= (remainder (square n) m) 1))))
