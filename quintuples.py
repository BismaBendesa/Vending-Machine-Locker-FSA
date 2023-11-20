"""Module for FSA Quintuplets"""

states = ["Q","A", "B", "C", "D", "E", "F", "G", "H", "I" ,"J", "K", "L", "M", "P", "R", "S", "T", "U", "N", "O",]
initialState = states[0]
finalStates = [states[states.index("U")], states[states.index("N")], states[states.index("O")], states[states.index("J")]] # U, N, O, J

transitionTable = {
    # a  b  c  d  e f
  0: [states[states.index("A")], states[states.index("B")], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # Q
  1: [0, 0, 0, 0, states[states.index("E")], states[states.index("F")], 0, 0, 0, 0, 0, 0, 0, 0, 0], # A
  2 :[0, 0, 0, 0, 0, 0, 0, 0, 0, states[states.index("P")], states[states.index("K")], 0, 0, 0], # B
  3 :[0, 0, 0, states[states.index("D")], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # C
  4 :[0, 0, 0, 0, 0, 0, 0, 0, states[states.index("J")], 0, 0, 0, 0, 0, 0], # D
  5 :[0, 0, 0, 0, 0, 0, 0, states[states.index("H")], 0, 0, 0, 0, 0, 0, 0], # E
  6 :[0, 0, 0, 0, 0, 0, states[states.index("G")], states[states.index("H")], 0, 0, 0, 0, 0, 0, 0], # F
  7 :[0, 0, 0, 0, 0, 0, states[states.index("H")], states[states.index("I")], 0, 0, 0, 0, 0, 0, 0], # G
  8 :[0, 0, states[states.index("C")], 0, 0, 0, states[states.index("H")], states[states.index("H")], 0, 0, 0, 0, 0, 0, 0], # H
  9 :[0, 0, states[states.index("C")], 0, 0, 0, states[states.index("I")], states[states.index("I")], 0, 0, 0, 0, 0, 0, 0], # I
  10 :[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # J (FINAL STATE)
  11 :[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, states[states.index("L")], states[states.index("M")], 0, 0], # K
  12 :[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, states[states.index("N")], 0], # L
  13 :[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, states[states.index("O")]], # M
  14 :[0, 0, 0, 0, 0, 0, 0, 0, 0, states[states.index("R")], states[states.index("K")], 0, 0, 0, 0], # P 
  15 :[0, 0, 0, 0, 0, 0, 0, 0, 0, states[states.index("S")], states[states.index("K")], 0, 0, 0, 0], # R
  16 :[0, 0, 0, 0, 0, 0, 0, 0, 0, states[states.index("T")], states[states.index("K")], 0, 0, 0, 0], # S
  17 :[0, 0, 0, 0, 0, 0, 0, 0, 0, states[states.index("U")], states[states.index("K")], 0, 0, 0, 0], # T
  18 :[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # U (FINAL STATE)
  19 :[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # N (FINAL STATE)
  20 :[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # O (FINAL STATE)
}
alphabetList = ["a", "b", "c", "d", "e", "f", "g", "h", "y", "m", "x", "w", "v", "u", "s"]

# input 
# a = pilih taruh barang
# b = pilih ambil barang
# c = input no telp
# d = input pilihan loker
# e = pilih Qris
# f = pilih tunai
# g = input uang 1000
# h = input uang 2000
# y = input yes
# m = input password salah
# x = no loker dan password
# w = pilih buka sementara
# v = pilih buka logout
# u = pilih tutup dan loker terisi
# s = pilih tutup dan loker kosong
# 0 = NULL
# k = kembalian
# t = tutup 
# n = kirim password ke nomor telepon sesuai loker
# z = warning password salah

