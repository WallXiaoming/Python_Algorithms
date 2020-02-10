class Code_01_BubbleSort:

    def main():

        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        def bubble_sort(arr):
            for i in range(len(arr) - 1, 0, -1):
                for j in range(i):
                    if arr[j] > arr[j + 1]:
                        swap(arr, j, j + 1)
            return arr

        def generator(length, irange):
            from random import randint
            return [randint(*irange) for _ in range(length)]

        def comparator(numTrial, length, irange):
            for _ in range(numTrial):
                arr = generator(length, irange)
                arr1 = sorted(arr)
                arr2 = bubble_sort(arr)
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
        a = [1, 2, 3, 3]
