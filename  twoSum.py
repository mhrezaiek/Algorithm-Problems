{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 class Solution:\
    def twoSum(self, nums: List[int], target: int) -> List[int]:\
        dic = \{\}\
        if len(nums)== 0 or len(nums) == 1:\
            return 0\
        for i , n in enumerate(nums):\
            dic[n]= i\
        \
        for i in range(len(nums)):\
            temp = target - nums[i]\
            if temp in dic and dic.get(temp)!=i:\
                return [i, dic.get(temp)]}