# p 267의 리스트 내포 및 진수 변환 문제

# 1 ~ 100 까지 숫자 중 2 진수 변환 시 0이 하나만 포함된 숫자를 찾고 그 숫자들의 합을 구하는 코드


# count 함수 및 리스트 내포를 적절히 사용하고 진수 변환까지 있는 볼만한 문제

output = [i
          for i in range(1, 100 + 1)
          if "{:b}".format(i).count('0') == 1
          ]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계 : ", sum(output))
