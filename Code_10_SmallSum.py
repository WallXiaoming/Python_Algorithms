class Code_10_SmallSum:

    def main():

        def merge(arr, left, mid, right):
            p1, p2, helparr, res = left, mid + 1, [], 0
            while p1 <= mid and p2 <= right:
                if arr[p1] < arr[p2]:
                    res += (right - p2 + 1) * arr[p1]
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
            return res

        def small_sum(arr, left, right):
            if left < right:
                p = left + (right - left) // 2
                return small_sum(arr, left, p) + small_sum(arr, p + 1, right) + merge(arr, left, p, right)
            return 0

        # for test
        def test():
            arr = [1, 3, 4, 2, 5]
            res = small_sum(arr, 0, len(arr) - 1)
            print(res)

        test()

    if __name__ == '__main__':
        main()
