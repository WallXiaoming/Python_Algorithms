class Code_05_QuickSort:

    def main():

        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        def partition(arr, left, right):
            from random import randint
            x = arr[randint(left, right)]
            less, more, p = left - 1, right + 1, left
            while p < more:
                if arr[p] < x:
                    less += 1
                    swap(arr, p, less)
                    p += 1
                elif arr[p] == x:
                    p += 1
                else:
                    more -= 1
                    swap(arr, p, more)
            return less, more

        def quick_sort(arr, left, right):
            if left < right:
                less, more = partition(arr, left, right)
                quick_sort(arr, left, less)
                quick_sort(arr, more, right)
                return arr

        def generator(length, irange):
            from random import randint
            return [randint(*irange) for _ in range(length)]

        def comparator(numTrial, length, irange):
            for _ in range(numTrial):
                arr = generator(length, irange)
                arr1 = sorted(arr)
                arr2 = quick_sort(arr, 0, len(arr) - 1)
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
