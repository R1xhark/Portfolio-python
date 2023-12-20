def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def print_array(arr):
    print("Aktuální pole: ", end="")
    for element in arr:
        print(element, end=" ")
    print()

def get_menu_choice():
    print("\nVyberte algoritmus řazení:")
    print("1. Bubble Sort (Třídění bublinkové)")
    print("2. Selection Sort (Třídění výběrem)")
    print("3. Insertion Sort (Třídění vkládáním)")
    print("4. Merge Sort (Slévání)")
    print("5. Quick Sort (Rychlé třídění)")
    print("6. Heap Sort (Třídění haldou)")
    print("0. Konec")
    choice = input("Zadejte volbu: ")
    return choice

def get_array_input():
    array_str = input("Zadejte prvky pole oddělené mezerami: ")
    array = array_str.split()
    return array

def main():
    array = get_array_input()

    while True:
        print_array(array)
        choice = get_menu_choice()

        if choice == "0":
            print("Ukončuji program.")
            break

        if choice == "1":
            bubble_sort(array)
            print(".")
        elif choice == "2":
            selection_sort(array)
            print("Pole seřazeno pomocí třídění výběrem.")
        elif choice == "3":
            insertion_sort(array)
            print("Pole seřazeno pomocí třídění vkládáním.")
        elif choice == "4":
            merge_sort(array)
            print("Pole seřazeno pomocí slévání.")
        elif choice == "5":
            array = quick_sort(array)
            print("Pole seřazeno pomocí rychlého třídění.")
        elif choice == "6":
            heap_sort(array)
            print("Pole seřazeno pomocí třídění haldou.")
        else:
            print("Neplatná volba. Zkuste to znovu.")

if __name__ == '__main__':
    main()
