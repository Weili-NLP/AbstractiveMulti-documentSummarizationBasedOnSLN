import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def compute_avg(rouge_file):
	sum_rouge_1 = 0.0
	sum_rouge_2 = 0.0
	sum_rouge_su4 = 0.0
	sys_ids = set()

	with open(rouge_file, 'r') as in_f:
		for line in in_f:
			strs = line.strip().split()

			if len(strs) != 8:
				continue
			if strs[2] != "Average_F:":
				continue

			sys_id = strs[0]
			rouge_metric = strs[1]
			rouge_val = float(strs[3])

			if rouge_metric not in ["ROUGE-1", "ROUGE-2", "ROUGE-SU4"]:
				continue

			if sys_id >= "A" and sys_id <= "Z":
				continue

			
			sys_ids.add(sys_id)

			print sys_id, rouge_metric, rouge_val
			print line

			if rouge_metric == "ROUGE-1":
				sum_rouge_1 += rouge_val
			elif rouge_metric == "ROUGE-2":
				sum_rouge_2 += rouge_val
			elif rouge_metric == "ROUGE-SU4":
				sum_rouge_su4 += rouge_val
			else:
				raise Exception(rouge_metric)

	print "avgDUC:"
	print "ROUGE-1: %.5f" % (sum_rouge_1 / len(sys_ids))
	print "ROUGE-2: %.5f" % (sum_rouge_2 / len(sys_ids))
	print "ROUGE-SU4: %.5f" % (sum_rouge_su4 / len(sys_ids))

compute_avg("rougejk.m.out")
