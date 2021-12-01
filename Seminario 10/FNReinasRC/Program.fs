open System
let crono = System.Diagnostics.Stopwatch()

// Devuelve el primer elemento de una lista
let Principio (list : 'a list) : 'a = 
    match list with
    | [] -> (-1, -1)
    | (p::resto) -> p

// Retorna la lista sin su primer elemento
let Resto (list : 'a list) : 'a list = 
    match list with
    | [] -> []
    | (p::resto) -> resto

// Revisa si dos reinas se amenzan en sus filas o columnas
let FilaColumna (x_1 : int, y_1 : int) (x_2 : int, y_2: int) : bool =
    x_1 = x_2 || y_1 = y_2

// Revisa si dos reinas se amenazan diagonalmente
let Diagonal (x_1 : int, y_1 : int) (x_2 : int, y_2: int) : bool =
    (x_1 - y_1) = (x_2 - y_2) || (x_1 + y_1) = (x_2 + y_2)

// Comprueba si las reinas se amenzan
let SeAmenazan (x_1 : int, y_1 : int) (x_2 : int, y_2: int) : bool =
    FilaColumna (x_1, y_1) (x_2, y_2) || Diagonal (x_1, y_1) (x_2, y_2)

// Comprueba si es posible poner una reina en una posicion
let rec PosiblePoner nPos puestas : bool =
    match puestas with
    | [] -> true
    | x::xs -> if SeAmenazan x nPos 
                    then false 
                else PosiblePoner nPos xs

// NReinasB función encargada de resolver el problema
// recibe la cantidad de reinas, el tablero con reinas puestas, 
// y la posicion actual (x,y)
let rec NReinasB (n : int) puestas (x: int) (y: int) : bool = 
    if y > n 
        then true 
    elif x > n && puestas = [] 
        then false 
    elif x > n 
        then
            let lResto = Resto puestas
            let (a, b) = Principio puestas
            NReinasB n (lResto) (a + 1) (y-1)
                elif PosiblePoner (x,y) puestas 
                    then NReinasB n ((x,y)::puestas) 1 (y+1)
                else NReinasB n puestas (x+1) y

// NReinas recibe n (cantidad de reinas y tablero nxn)
let NReinas (n: int) : bool  = NReinasB n [] 1 1

crono.Start()
System.Console.WriteLine(NReinas (8))
crono.Stop()
System.Console.WriteLine("Time elapsed: {0}", crono.Elapsed);;
crono.Reset()