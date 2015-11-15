(defn mylast [coll]
    (if ( = 0 (count coll))
      nil)
    (if (= 1 (count coll))
      (first coll))
    (myLast (next coll)))

(defn mySum [coll] temp
  (if ( = 0 (count coll)
        temp)
    ( + temp (mySum (next coll)))))

(defn sum [coll]
  (if (= 0 (count coll))
    0
    (+ (first coll) (sum (next coll)))))

(defn mybutlast [coll]
  (if (= 1 (count coll))
    nil
    (cons (first coll) (mybutlast (next coll)))))

(defn myevens [coll]
  (if (= 0 (count coll))
    nil
    (if ( > 1 (count coll))
      (cons (first coll) (myevens (next coll)))
      (myevens (next coll)))))

(defn third [coll]
  (if (> 3 (count coll))
    nil
    (first (next (next coll)))))