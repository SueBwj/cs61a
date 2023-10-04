(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)


(define (sign num)
  (cond 
    ((> num 0) (display 1))
    ((= num 0) (display 0))
    ((< num 0) (display -1))
  )
)


(define (square x) (* x x))

(define (pow x y)
  (cond
    ((= x 1) 1)
    ((= y 0) 1)
    ;;;就像递归一样，在y=0的时候要返回值
    ((> y 0) (* x (pow x (- y 1))))
  )
)

