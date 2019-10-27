import glob
import read_file

numfour = glob.glob('/Users/yota/PycharmProjects/kishimoto_1020/csv_data/active_rate/active_no4/*')
numfive = glob.glob('/Users/yota/PycharmProjects/kishimoto_1020/csv_data/active_rate/active_no5/*')
hertfour = glob.glob('/Users/yota/PycharmProjects/kishimoto_1020/csv_data/heart_rate/heart_no4/*')
hertfive = glob.glob('/Users/yota/PycharmProjects/kishimoto_1020/csv_data/heart_rate/heart_no5/*')


numfour = sorted(numfour)
numfive = sorted(numfive)
hertfour = sorted(hertfour)
hertfive = sorted(hertfive)

for i in range(0,len(numfour)):
    read_file.read_and_write_file(hertfour[i], numfour[i])