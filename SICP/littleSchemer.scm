#lang scheme

;; ~~~LAWS~~~
;; Law of Car: The primitive 'car' is defined only for non-empty lists.
;; Law of Cdr: The primitive 'cdr' is efined only for non-empty lists. The cdr of any non-empty list is always another list.
;; Law of Cons: The primitive 'cons' takes two arguments. The second must be a list. The result is a list.
;; Law of Null?: The primitive 'null?' is defined only for lists.
;; Law of Eq?: The primitive 'eq?' takes two arguments. Each must be a non-numeric atom.

;; ~~~COMMANDMENTS~~~
;; First Commandment: Always ask 'null?' as the first question in expressing any function.
;;                    When recurring on a list of atoms, 'lat', ask two questions: '(null? lat)' and 'else'.
;;                    When recurring on a number, 'n', ask two questions: '(zero? n)' and 'else'.  
;; Second Commandment: Use 'cons' to build lists.
;; Third Commandment: When building a list, describe the first typical element, and the cons it onto the natural    
;;                    recursion.
;; Fourth Commandment: Always change at least one argument while recurring. The changing argument must be tested in 
;;                     the terminating condition. If using 'cdr', ask 'null?'. If using 'sub1', ask 'zero?'. 

;; ~~~CODE~~~
;; atom?: strings of characters not enclosed by ()
(define atom?
  (lambda (x)
    (and (not (pair? x))
         (not (null? x)))))

;; lat?: lists whose individual members are all atoms
(define lat? 
  (lambda (l)
    (cond
      ((null? l) true)
      ((atom? (car l)) (lat? (cdr l)))
      (else false))))

;; member?: is the atom 'a' a member of the list of atoms 'lat'?
(define member? 
  (lambda (a lat)
    (cond
      ((null? lat) false)
      (else (or (eq? (car lat) a)
                (member? a (cdr lat)))))))

;; rember: remove first occurrence of 'a' in 'lat'.
(define rember  
  (lambda (a lat)
    (cond
      ((null? lat) (quote ()))
      ((eq? (car lat) a) (cdr lat))
      (else (cons (car lat)
                  (rember a (cdr lat)))))))

;; firsts: Takes a list of non-empty lists (or a null list)
;; and returns a list with the first S-exp of each list.
(define firsts      
  (lambda (l) 
    (cond
      ((null? l) (quote ()))
      (else (cons (car (car l))
                  (firsts (cdr l)))))))

;; seconds: Takes a list of non-empty lists (or a null list) and
;; returns a list with the second S-exp of each list.
(define seconds    
  (lambda (l)      
    (cond
      ((null? l) (quote ()))
      (else (cons (car (cdr (car l)))
                  (seconds (cdr l)))))))

;; insertR: Inserts the atom 'new' to the right of the atom 'old' in the list 'lat'.
(define insertR        
  (lambda (new old lat)
    (cond ((null? lat) (quote ()))
          ((eq? (car lat) old) (cons old (cons new (cdr lat))))
          (else (cons (car lat)
                      (insertR new old (cdr lat)))))))

;; insertL: Inserts the atom 'new' to the right of the atom 'old' in the list 'lat'.
(define insertL       
  (lambda (new old lat)
    (cond ((null? lat) (quote ()))
          ((eq? (car lat) old) (cons new lat))
          (else (cons (car lat)
                      (insertL new old (cdr lat)))))))

;; subst: Replaces the atom 'old' for the atom 'new' in the list 'lat'.
(define subst         
  (lambda (new old lat)
    (cond ((null? lat) (quote ()))
          ((eq? (car lat) old) (cons new (cdr lat)))
          (else (cons (car lat)
                      (subst new old (cdr lat)))))))

;; subst2: Replaces either the first occurrence of 'o1' or that of 'o2' by 'new'.
(define subst2        
  (lambda (new o1 o2 lat)
    (cond
      ((null? lat) (quote ()))
      ((or (eq? (car lat) o1)
           (eq? (car lat) o2)) (cons new (cdr lat)))
      (else (cons (car lat) (subst2 new o1 o2 (cdr lat)))))))

;; multirember: removes all occurrences of 'a' from 'lat'
(define multirember
  (lambda (a lat)
    (cond
      ((null? lat) (quote ()))
      ((eq? (car lat) a) (multirember a (cdr lat)))
      (else (cons (car lat) (multirember a (cdr lat)))))))

;; multiinsertR: inserts 'new' to the right of all 'old' in 'lat'
(define multiinsertR
  (lambda (new old lat)
    (cond
      ((null? lat) (quote ()))
      ((eq? (car lat) old) (cons old
                                 (cons new (multiinsertR new old (cdr lat)))))
      (else (cons (car lat) (multiinsertR new old (cdr lat)))))))

;; multiinsertL: inserts 'new' to the left of all 'old' in 'lat'
(define multiinsertL
  (lambda (new old lat)
    (cond
      ((null? lat) (quote ()))
      ((eq? (car lat) old) (cons new
                                 (cons old
                                       (multiinsertL new old (cdr lat)))))
      (else (cons (car lat) (multiinsertL new old (cdr lat)))))))

;; multisubst: replaces all instances of 'old' in 'lat' by 'new'.
(define multisubst
  (lambda (new old lat)
    (cond
      ((null? lat) (quote ()))
      ((eq? (car lat) old) (cons new (multisubst new old (cdr lat))))
      (else (cons (car lat) (multisubst new old (cdr lat)))))))

;; add1: adds 1 to a number.
(define add1
  (lambda (n)
    (+ n 1)))

;; sub1: substracts 1 from a number.
(define sub1
  (lambda (n)
    (- n 1)))

;; o+: sums two numbers.
(define o+
  (lambda (n m)
    (cond
      ((zero? m) n)
      (else (o+ (add1 n)
                (sub1 m))))))

;; o-: returns the difference between two numbers
(define o-
  (lambda (n m)
    (cond
      ((zero? m) n)
      (else (o- (sub1 n)
                (sub1 m))))))

;; addtup: builds a number by adding all numbers in a given tup
(define addtup
  (lambda (tup)
    (cond
      ((null? tup) 0)
      (else (+ (car tup)
               (addtup (cdr tup)))))))

;; o*; add up a number 'n', 'm' times.
(define o*
  (lambda (n m)
    (cond ((zero? m) 0)
          (else (+ n (o* n (sub1 m)))))))