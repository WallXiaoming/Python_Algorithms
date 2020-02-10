class Code_07_BucketSort:

    def main():

        # from numpy import arrary

        def bucket_sort(arr):
            if arr == [] or len(arr) < 2:
                return arr
            bucket = [0 for _ in range(max(arr) + 1)]
            for i in arr:
                bucket[i] += 1
            i = 0
            for j in range(len(bucket)):
                while bucket[j] > 0:
                    arr[i] = j
                    bucket[j] -= 1
                    i += 1
            return arr

        def generator(length, irange):
            from random import randint
            return [randint(*irange) for _ in range(length)]

        def comparator(numTrial, length, irange):
            for _ in range(numTrial):
                arr = generator(length, irange)
                arr1 = sorted(arr)
                arr2 = bucket_sort(arr)
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
