class Code_02_SelectSort:

    def main():

        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        def select_sort(arr):
            n = len(arr)
            for i in range(n - 1):
                k = i
                for j in range(i, n):
                    if arr[j] < arr[k]:
                        k = j
                swap(arr, k, i)
            return arr

        def generator(length, irange):
            from random import randint
            return [randint(*irange) for _ in range(length)]

        def comparator(numTrial, length, irange):
            for _ in range(numTrial):
                arr = generator(length, irange)
                arr1 = sorted(arr)
                arr2 = select_sort(arr)
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
        a = [1, 2, 2]
        b = [12, 23, 1]
