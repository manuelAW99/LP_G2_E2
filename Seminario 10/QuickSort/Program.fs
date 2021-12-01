// Función dedicada a devolver los menores que un valor en una lista
let rec MenorQP (list: 'a list) (pivote : 'a) : 'a list =
    match list with
    | [] -> []
    | (x::lista) -> if x < pivote then x::MenorQP lista pivote else MenorQP lista pivote

// Función dedicada a devolver los mayores que un valor en una lista
let rec MayorQP (list : 'a list) (pivote : 'a) : 'a list =
    match list with
    | [] -> []
    | (x::lista) -> if x >= pivote then x::MayorQP lista pivote else MayorQP lista pivote

// Algoritmo de QuickSort
let rec QuickSort (list : 'a list) : 'a list = 
    match list with
    | [] -> []
    | (pivote::lista) -> QuickSort(MenorQP lista pivote) @ [pivote] @ QuickSort(MayorQP lista pivote)
                     
let lista = QuickSort [55;-22;1;2;3;0]
for num in lista do
    printf "%A " num
    
printfn ""