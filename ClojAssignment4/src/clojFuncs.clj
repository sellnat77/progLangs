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