[<AllowNullLiteral>] 
type Nodo (valor, hijoIzq : Nodo, hijoDer : Nodo) =
    member this.valor = valor 
    member this.hijoIzq = hijoIzq
    member this.hijoDer = hijoDer

let rec Agregar (nodo : Nodo) (nValor : IComparable) : Nodo = 
    match nodo with
    | null -> Nodo(nValor, null, null)
    | nodo when nodo.valor < nValor -> Nodo(nodo.valor, nodo.hijoIzq, Agregar nodo.hijoDer nValor)
    | nodo when nodo.valor > nValor -> Nodo(nodo.valor, Agregar nodo.hijoIzq nValor,  nodo.hijoDer)
    | nodo when nodo.valor = nValor -> Nodo(nodo.valor, nodo.hijoIzq,  nodo.hijoDer)

let rec Contiene (nodo : Nodo) (valor : IComparable) : bool = 
    match nodo with
    | null -> false
    | nodo when nodo.valor < valor -> Contiene nodo.hijoDer valor
    | nodo when nodo.valor > valor -> Contiene nodo.hijoIzq valor
    | nodo when nodo.valor = valor -> true