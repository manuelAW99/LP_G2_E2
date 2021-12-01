using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace NReinas {
    class Program {
        static void Main(string[] args) {
            Stopwatch s = new Stopwatch();
            s.Start();
            Console.WriteLine(NReinas(8));
            s.Stop();
            Console.WriteLine(s.Elapsed);
            
        }
        public static bool NReinas(int n) {
            return NReinas(new List<(int, int)>(), 1, n);
        }
        public static bool NReinas(List<(int, int)> puestas, int columna, int n) {
            if (columna == n + 1) return true;

            for (int fila = 1; fila <= n; fila++) {
                if (PosiblePoner(new Tuple<int, int>(fila, columna), puestas)) {
                    puestas.Add((fila, columna));
                    if (NReinas(puestas, columna + 1, n))
                        return true;
                    puestas.Remove((fila, columna));
                }
            }
            return false;
        }
        public static bool PosiblePoner(Tuple<int, int> nPos, List<(int, int)> reinas) {
            foreach (var pReina in reinas) {
                int fila = pReina.Item1;
                int columna = pReina.Item2;

                if (SeAmenazan(fila, columna, nPos.Item1, nPos.Item2)) return false;
            }
            return true;
        }  
        public static bool SeAmenazan(int x_1, int y_1, int x_2, int y_2) {
            return FilaColumna(x_1,y_1,x_2,y_2) || Diagonal(x_1,y_1,x_2,y_2);
        }
        public static bool Diagonal(int x_1, int y_1, int x_2, int y_2) {
            return x_1 - y_1 == x_2 - y_2 || x_1 + y_1 == x_2 + y_2;
        }
        public static bool FilaColumna(int x_1, int y_1, int x_2, int y_2) {
            return x_1 == x_2 || y_1 == y_2 || x_1 - y_1 == x_2 - y_2;
        }
              
    }
}

