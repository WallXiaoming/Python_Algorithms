class Code_08_RadixSort:

    def main():

        def radix_sort(arr):
            digit = len(str(max(arr)))
            n = len(arr)
            for d in range(1, digit + 1):
                count = [0 for _ in range(10)]
                bucket = [0 for _ in range(n)]
                for i in arr:
                    j = getDigit(i, d)
                    count[j] += 1
                for i in range(1, 10):
                    count[i] = count[i] + count[i - 1]
                for i in range(n - 1, -1, -1):
                    j = getDigit(arr[i], d)
                    bucket[count[j] - 1] = arr[i]
                    count[j] -= 1
                for i in range(n):
                    arr[i] = bucket[i]
            return arr

        def getDigit(number, d):
            return int(number / pow(10, d - 1)) % 10

        def generator(length, irange):
            from random import randint
            return [randint(*irange) for _ in range(length)]

        def comparator(numTrial, length, irange):
            for _ in range(numTrial):
                arr = generator(length, irange)
                arr1 = sorted(arr)
                arr2 = radix_sort(arr)
                if arr1 != arr2:
                    print('Fu....')
                    print('arr1:', arr1)
                    print('arr2:', arr2)
                    break
            else:
                print('Nice')

        comparator(1000, 100, [10, 100])

    if __name__ == '__main__':
        main()
