class Code_03_InsertSort:

    def main():

        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        def insert_sort(arr):
            for i in range(1, len(arr)):
                j = i - 1
                while j >= 0 and arr[j] > arr[j + 1]:
                    swap(arr, j, j + 1)
                    j -= 1
            return arr

        def generator(length, irange):
            from random import randint
            return [randint(*irange) for _ in range(length)]

        def comparator(numTrial, length, irange):
            for _ in range(numTrial):
                arr = generator(length, irange)
                arr1 = sorted(arr)
                arr2 = insert_sort(arr)
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
