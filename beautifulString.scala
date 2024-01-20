def beautifulString(inputString: String): Boolean = {
  val valuesCnt = inputString.groupMapReduce(identity)(_ => 1)(_ + _)

  val alphabet = 'a' to 'z'

  val valuesCntAlphabet = alphabet.map(let => valuesCnt.getOrElse(let,0))

  val isBeautiful = valuesCntAlphabet.zip(valuesCntAlphabet.tail).forall{case (a,b) => a>= b}
  isBeautiful
}
