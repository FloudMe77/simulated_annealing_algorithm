# Simulated Annealing Algorithm  
**Autor:** Dariusz Marecik, grupa 6, godz. 16:45

<!-- ## Opis projektu

Repozytorium zawiera implementację i wyniki działania algorytmu **symulowanego wyżarzania** (simulated annealing) dla trzech różnych problemów optymalizacyjnych:

- Problem komiwojażera (TSP)
- Tworzenie struktur krystalicznych
- Rozwiązywanie Sudoku

--- -->

## Struktura repozytorium

### Pliki `.ipynb`
Zawierają sprawozdania i szczegółowe omówienie każdego z zadań.

### Folder `zad1_gifs`
Zawiera animacje przedstawiające przebieg działania algorytmu dla problemu komiwojażera (TSP), pokazujące proces wyszukiwania najkrótszego cyklu.

### Folder `zad2_images`
Zawiera wyniki związane z tworzeniem sieci krystalicznych. Struktura folderów:
- `gifs/` – animacje przedstawiające proces tworzenia się sieci krystalicznej dla każdej z analizowanych struktur.
- `images/` – obrazy końcowych efektów generowania sieci krystalicznych.
- `plots/` – wykresy funkcji optymalizowanych podczas tworzenia struktur.

Każdy z powyższych folderów zawiera podkatalogi nazwane zgodnie z nazwami omawianych sieci krystalicznych.

### Folder `zad3_sudoku`
Zawiera dane i wyniki testów rozwiązywania Sudoku:
- `figs/` – wykresy funkcji błędów w czasie działania algorytmu.
- `sudoku/` – pliki z nierozwiązanymi planszami Sudoku (dane wejściowe).
- `sudoku_results/` – plansze Sudoku rozwiązane przez algorytm.

Każdy zestaw testowy posiada osobny katalog zawierający powyższe trzy foldery.