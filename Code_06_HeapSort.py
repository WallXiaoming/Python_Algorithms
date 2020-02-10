class Code_06_HeapSort:

    def main():

        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        def heapify(arr, i, r):
            left, right = 2 * i + 1, 2 * i + 2
            if right <= r and arr[left] < arr[right] and arr[right] > arr[i]:
                largest = right
            elif left <= r and arr[left] > arr[i]:
                largest = left
            else:
                largest = i
            if largest != i:
                swap(arr, largest, i)
                heapify(arr, largest, r)

        def build_heap(arr, left, right):
            mid = left + (right - left) // 2
            for i in range(mid, -1, -1):
                heapify(arr, i, right)

        def heap_sort(arr, left, right):
            build_heap(arr, left, right)
            for i in range(right, 0, -1):
                swap(arr, 0, i)
                heapify(arr, 0, i - 1)
            return arr

        def generator(length, irange):
            from random import randint
            return [randint(*irange) for _ in range(length)]

        def comparator(numTrial, length, irange):
            for _ in range(numTrial):
                arr = generator(length, irange)
                arr1 = sorted(arr)
                arr2 = heap_sort(arr, 0, len(arr) - 1)
                if arr1 != arr2:
                    print('Fu....')
                    print('arr1:', arr1)
                    print('arr2:', arr2)
                    break
            else:
                print('Nice')

        comparator(1000, 10, [10, 100])

    if __name__ == '__main__':
        main()
