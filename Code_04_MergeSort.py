class code_05_MergeSort:

    def main():

        def merge(arr, left, mid, right):
            p1, p2, helparr = left, mid + 1, []
            while p1 <= mid and p2 <= right:
                if arr[p1] < arr[p2]:
                    helparr.append(arr[p1])
                    p1 += 1
                else:
                    helparr.append(arr[p2])
                    p2 += 1
            while p1 <= mid:
                helparr.append(arr[p1])
                p1 += 1
            while p2 <= right:
                helparr.append(arr[p2])
                p2 += 1
            arr[left:right + 1] = helparr

        def merge_sort(arr, left, right):
            if left < right:
                p = (left + right) // 2
                merge_sort(arr, left, p)
                merge_sort(arr, p + 1, right)
                merge(arr, left, p, right)
                return arr

        def generator(length, irange):
            from random import randint
            return [randint(*irange) for _ in range(length)]

        def comparator(numTrial, length, irange):
            for _ in range(numTrial):
                arr = generator(length, irange)
                arr1 = sorted(arr)
                arr2 = merge_sort(arr, 0, len(arr) - 1)
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
