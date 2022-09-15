A = 0.65 #left Foot edge activation in acccented stem
mpl = 0.5 #Max-path left edge of Foot
dpl = 0.5 #Dep-path left edge of Foot
ml = 0.1 #Max Left edge of Foot
dl = 0.5 #Dep left edge of Foot
ar = 0.5 #Align Foot right (rewarded if satisfied)
dpr = 0.5 #Dep-path right edge of Foot
dr = 0.5 #Dep right edge of Foot
mpr = 0.5 #Max-path right edge of Foot
mr = 0.1 #Max-right edge of Foot
Sl = .875 #Left Foot edge activation on dominant "stressless"
Sr = .25 #Right Foot edge activation on dominant "stressless"
u = .1 #Uniformity. Violated if two Foot edges coalesce.
dep_anch_left_stem = 4.0 #If a Foot occurs at the left edge of the word in the output, there must be a corresponding left Foot edge at the left edge of the stem in the input 
anch_r_ft_edge = 0.6 #A right Foot edge in the input must have a corresponding right Foot edge in the output, just in case the site of that potential Foot edge occurs qwithin a Foot in the output.
R = 0.5 #Activation of the left Foot edge of a recessive preaccenting suffix
D = .75 #Activation of the left Foot edge of a dominant preaccenting suffix
lr = 1/16 #Learning rate

for epoch in range(30):
    print('\nepoch *******************', epoch)
    num_tested = 0
    num_correct = 0
    print('\n(AAA')
    num_tested += 1
    f1 = A*mpl + A*ml -dl*(1-A) -(1-A)*dpl -dpr -dr
    f2 =         A*ml -dl*(1-A)       -dpl -dpr -dr  +ar
    print(round(f1, 4), round(f2, 4))
    if f1 > f2:
        num_correct += 1
        print('CORRECT')
    else:
        if A < 1 -lr:
            A += lr
            print('Increasing A')
        mpl += lr
        print('Increasing mpl')

    print('\n(AA(S)')
    num_tested += 1
    f1 = A*ml +A*mpl -(1-A)*dpl -(1-A)*dl     -dr       -dpr
    f2 = A*ml             -dpl  -dl*(1-A) -dr*(1-Sr) -dpr*(1-Sr) + Sr*mr +Sr*mpr +ar
    print(round(f1, 4), round(f2, 4))
    #print(A*ml, A*mpl, -(1-A)*dpl, -dpl, -(1-A)*dl, -dr, -dr*(1-Sr), Sr*mr, Sr*mpr, ar)
    #print(A, mpl, A*mpl)
    if f1 < f2:
        num_correct += 1
        print('CORRECT')
    else:
        if Sr < 1 - lr:
            Sr += lr
            print('Increasing Sr')
        if A > lr:
            A -+ lr
            print('Decreasing A')
        mpl -= lr
        dpl -= lr

    print('\nUU(S)')
    num_tested += 1
    f1 =  -dl        -dpl                 -dr        -dpr -dep_anch_left_stem  #(UU)S
    f2 =  -dl*(1-Sl) -dpl  +Sr*mr +Sr*mpr -dr*(1-Sr) -dpr*(1-Sr) + ar #U(US)
    print(round(f1, 4), round(f2, 4))
    if f2 > f1:
        num_correct += 1
        print('CORRECT')

    print('\n(AA(S)N')
    num_tested += 1
    f1 = A*mpl +A*ml   -(1-A)*dpl -(1-A)*dl     -dr       -dpr #(AA)SN
    f2 =       +A*ml       -dpl    -dl*(1-A)   -dr*(1-Sr) -dpr*(1-Sr) +mpr*Sr +mr*Sr #A(AS)N
    f3 = mpl*Sl +ml*Sl -dpl*(1-Sl) -dl*(1-Sl) -dr*(1-Sr) -dpr + ar            +mr*Sr #AA(SN)
    if f3 > max(f1, f2):
        num_correct += 1
        print('CORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4))
    else:
        print('INCORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4))
        ar += lr
        A -= lr
        Sr -= lr
        Sl += lr
        mr += lr
        mpr -= lr
        dpr -= lr
        print('Increasing ar, Sl and mr; dedcreasing A, Sr, mpr and dpr.')

    print('\n(AA(S)(S)N')
    num_tested += 1
    f1 = A*mpl +A*ml -(1-A)*dpl     -(1-A)*dl    -dr        -dpr #(AA)SSN
    f2 =       +A*ml      -dpl      -dl*(1-A)    -dr*(1-Sr) -dpr*(1-Sr) +mr*Sr +mpr*Sr  #A(AS)SN
    f3 = Sl*mpl +Sl*ml     -dpl*(1-Sl) -dl*(1-Sl) -dr*(1-Sr)  -dpr*(1-Sr) +mr*Sr +mpr*Sr  -anch_r_ft_edge*Sr       #AA(SS)N
    f4 = Sl*mpl +Sl*ml     -dpl*(1-Sl) -dl*(1-Sl) -dr*(1-Sr)  -dpr        +mr*Sr          -anch_r_ft_edge*Sr   +ar #AAS(SN)
    if f4 > max(f1, f2, f3):
        num_correct += 1
        print('CORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4), round(f4, 4))
    else:
        print('INCORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4), round(f4, 4))
        ar += lr
        print('Increasing ar')

    print('\nUUR)R)')
    num_tested += 1
    f1 = -dpl -dl               -dr       -dpr     -dep_anch_left_stem            #(UU)RR
    f2 = -dpl -dl +mr*R  +mpr*R -dr*(1-R) -dpr*(1-R)        #U(UR)R
    f3 = -dpl -dl +mr*R  +mpr*R -dr*(1-R) -dpr*(1-R)  +ar -anch_r_ft_edge*R    #UU(RR)
    if f2 > max(f1,f3):
        num_correct += 1
        print('CORRECT')
        print('ar', ar, 'anchor', anch_r_ft_edge, 'r', R, round(f1, 4), round(f2, 4), round(f3, 4))
    else:
        print('INCORRECT')
        print('ar', ar, 'anchor', anch_r_ft_edge, 'r', R, round(f1, 4), round(f2, 4), round(f3, 4))
        anch_r_ft_edge += lr
        R += lr
        print('Increasing anch_r_ft_edge and R.')
        #ar -= lr

    print('\n(AAD)D)R))')
    num_tested += 1
    f1 = A*mpl +ml*A    -(1-A)*dpl -(1-A)*dl                    -dr -dpr                                                          #(AA)DDR
    f2 =        +ml*A   -dpl        -dl*(1-A)   +mr*D +mpr*D    -dr*(1-D)          -dpr*(1-D)                                     #A(AD)DR
    f3 =                -dpl        -dl         +mr*D +mpr*D    -dr*(1-D)          -dpr*(1-D)          -anch_r_ft_edge*D          #AA(DD)R
    f4 =                -dpl        -dl         +mr*D           -dr*(1-max(R,D))    -dpr*(1-R)         +ar  -anch_r_ft_edge*D     #AAD(DR)
    if f2 > max(f1, f3, f4):
        num_correct += 1
        print('CORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4), round(f4, 4))
    else:
        print('INCORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4), round(f4, 4))


    print('\nUUR)D)D)')
    num_tested += 1
    f1 =   -dpl -dl -dpr       -dr                                         -dep_anch_left_stem      #(UU)RDD
    f2 =   -dpl -dl -dpr*(1-R) -dr*(1-D)          +mpr*R +mr*max(R,D)                               #U(UR)DD
    f3 =   -dpl -dl -dpr*(1-D) -dr*(1-max(R,D))   +mpr*D +mr*max(D,R) -anch_r_ft_edge*R             #UU(RD)D
    f4 =   -dpl -dl -dpr*(1-D) -dr*(1-max(R,D))   +mpr*D +mr*max(D,R) -anch_r_ft_edge*D +ar         #UUR(DD)
    if f3 > max(f1, f2, f4):
        num_correct += 1
        print('CORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4), round(f4, 4))
    else:
        print('INCORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4), round(f4, 4))
        if D < 1 - lr:
            D += lr
            print('Increasing D')
        if R > lr:
            R -= lr
            print('Decreasing R.')

    print('\n(AA(S)NR)')
    num_tested += 1
    f1 = A*mpl    +A*ml  -(1-A)*dpl    -(1-A)*dl -dr                    -dpr #(AA)SNR
    f2 =           A*ml        -dpl   - dl*(1-A) -dr*(1-Sr)             -dpr*(1-Sr)   +mr*Sr             +mpr*Sr #A(AS)NR
    f3 =   Sl*mpl  +Sl*ml  -(1-Sl)*dpl  -(1-Sl)*dl -dr*(1-max(Sr,R))    -dpr          +mr*max(Sr,R)                      -anch_r_ft_edge*Sr #AA(SN)R
    f4 =           +Sl*ml  -dpl        -(1-Sl)*dl -dr*(1-max(Sr,R))      -dpr*(1-R)   +mr*max(Sr,R)      +mpr*R                +ar #AAS(NR)
    if f4 > max(f1, f2, f3):
        num_correct += 1
        print('CORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4), round(f4, 4))
    else:
        print('INCORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4), round(f4, 4))
        anch_r_ft_edge += lr
        Sr += lr
        print('Increasing anch_rtr_ft_edge and Sr.')

    print('\n(AANNR)')
    num_tested += 1
    f1 = A*mpl +A*ml -(1-A)*dpl -(1-A)*dl    -dr       -dpr #(AA)NNR
    f2 =        A*ml        -dpl   -dl*(1-A) -dr*(1-R) -dpr  +mr*R #A(AN)NR
    f3 =                    -dpl  -dl        -dr*(1-R)  -dpr +mr*R #AA(NN)R
    f4 =                    -dpl   -dl       -dr*(1-R)   -dpr*(1-R) +mr*R +mpr*R +ar #AAN(NR)
    if f1 > max(f2,f3,f4):
        num_correct += 1
        print('CORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4), round(f4, 4))
    else:
        print('INCORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4), round(f4, 4))
        A += lr
        print('Increasing A.')

    print('\n(AAN')
    num_tested += 1
    f1 = A*mpl +A*ml -(1-A)*dpl -(1-A)*dl -dr -dpr #(AA)N
    f2 =       +A*ml      -dpl  -(1-A)*dl -dr -dpr +ar #A(AN) 
    if f1 > f2:
        num_correct += 1
        print('CORRECT')
        print(round(f1, 4), round(f2, 4))
    else:
        print('INCORRECT')
        print(round(f1, 4), round(f2, 4))
    
    print('\nUNN')
    num_tested += 1
    f1 = -dpl -dl  -dpr -dr -dep_anch_left_stem #(UN)N
    f2 = -dpl -dl -dpr -dr +ar #U(NN)
    print(round(f1, 4), round(f2, 4))
    if f2 > f1:
        num_correct += 1
        print('CORRECT')
    else:
        print('INCORRECT')

    print('\nUN(S)')
    num_tested += 1
    f1 =       -dpl -dl        -dpr        -dr*(1-Sr) +mr*Sr -dep_anch_left_stem #(UN)S
    f2 = ml*Sl -dpl -dl*(1-Sl) -dpr*(1-Sr) -dr*(1-Sr) +mr*Sr  +Sr*mpr +ar #U(NS)
    print(round(f1, 4), round(f2, 4))
    if f2 > f1:
        num_correct += 1
        print('CORRECT')
    else:
        print('INCORRECT')

    print('\n(AANN(S)')
    num_tested += 1
    f1 = A*mpl +A*ml -(1-A)*dpl -(1-A)*dl -dr         -dpr #(AA)NNS
    f2 =       +A*ml      -dpl  -(1-A)*dl -(1-Sr)*dr  -dpr        +Sr*mr #A(AN)NS
    f3 =       +Sl*ml     -dpl  -(1-Sl)*dl -(1-Sr)*dr -dpr        +Sr*mr#AA(NN)S
    f4 =       +Sl*ml     -dpl  -(1-Sl)*dl -(1-Sr)*dr -(1-Sr)*dpr +Sr*mr  +Sr*mpr +ar #AAN(NS)
    if f4 > max(f1, f2, f3):
        num_correct += 1
        print('CORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4), round(f4, 4))
    else:
        print('INCORRECT')
        Sr += lr
        print('Increasing Sr.')
        print(round(f1, 4), round(f2, 4), round(f3, 4), round(f4, 4))


    print('\nUU(S)(S)')
    num_tested += 1
    f1 =               -dpl         -dl          -dpr        -dr          -dep_anch_left_stem #(UU)SS
    f2 =                -dpl        -dl          -dpr*(1-Sr) -dr*(1-Sr) + Sr*mr + Sr*mpr #U(US)S
    f3 = ml*Sl + mpl*Sl -dpl*(1-Sl) -dl*(1-Sl)   -dpr*(1-Sr) -dr*(1-Sr) +Sr*mr +Sr*mpr +ar -anch_r_ft_edge*Sr #UU(SS)
    #print(ml*Sl, mpl*Sl, dl*(1-Sl), dpl*(1-Sl), mr*Sr, mpr*Sr, dr*(1-Sr), dpr*(1-Sr), ar, anch_r_ft_edge*Sr)
    if f3 > max(f1, f2):
        num_correct += 1
        print('CORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4))
    else:
        print('INCORRECT')
        Sr += lr
        print('Increasing Sr.')
        print(round(f1, 4), round(f2, 4), round(f3, 4))

    print('\n(AA(S)(S)')
    num_tested += 1
    f1 = A*mpl    +A*ml -(1-A)*dpl -(1-A)*dl    -dr        -dpr #(AA)SS
    f2 =           A*ml -dpl       -dl*(1-A)    -dr*(1-Sr) -dpr*(1-Sr) +Sr*mpr +Sr*mr #A(AS)S
    f3 = +mpl*Sl  +ml*Sl -dpl*(1-Sl) -dl*(1-Sl) -dr*(1-Sr) -dpr*(1-Sr) +Sr*mpr +Sr*mr +ar -anch_r_ft_edge*Sr #AA(SS)
    if f3 > max(f1, f2):
        num_correct += 1
        print('CORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4))
    else:
        print('INCORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4))
        ar += lr
        Sr -= lr
        print('Increasing ar and decreasing Sr.')

    print('\n(AAR)')
    num_tested += 1
    f1 = A*mpl +A*ml -(1-A)*dpl -(1-A)*dl -dr       -dpr                         #(AA)R
    f2 =        A*ml       -dpl -dl*(1-A) -dr*(1-R) -dpr*(1-R) +R*mpr + R*mr +ar #A(AR)
    if f1 > f2:
        num_correct += 1
        print('CORRECT')
        print(round(f1, 4), round(f2, 4))
    else:
        print('INCORRECT')
        print(round(f1, 4), round(f2, 4))
        dpl += lr
        print('Increasing dpl')

    print('\n(AAR)R)')
    num_tested += 1
    f1 = A*mpl +A*ml -(1-A)*dpl -(1-A)*dl   -dr        -dpr                                             #(AA)RR
    f2 =        A*ml -dpl        -dl*(1-A)  -dr*(1-R)  -dpr*(1-R) +R*mpr +R*mr                           #A(AR)R
    f3 =             -dpl        -dl        -dr*(1-R)  -dpr*(1-R) +R*mpr +R*mr  +ar  -anch_r_ft_edge*R   #AA(RR)
    if f1 > max(f2, f3):
        num_correct += 1
        print('CORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4))
    else:
        print('INCORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4))
        #ar += lr

    print('\n(ANR)')
    num_tested += 1
    f1 = A*mpl +A*ml -(1-A)*dpl -(1-A)*dl -dr       -dpr                         #(AN)R
    f2 =                   -dpl -dl       -dr*(1-R) -dpr*(1-R) +R*mpr + R*mr +ar #A(NR)
    if f1 > f2:
        num_correct += 1
        print('CORRECT')
        print(round(f1, 4), round(f2, 4))
    else:
        print('INCORRECT')
        print(round(f1, 4), round(f2, 4))

    print('\n(AA(S)R)')
    num_tested += 1
    f1 = A*mpl +A*ml -(1-A)*dpl -(1-A)*dl -dr                     -dpr #(AA)SR
    f2 =        A*ml        -dpl -dl*(1-A) -dr*(1-Sr)             -dpr*(1-Sr) + mpr*Sr + mr*Sr #A(AS)R
    f3 = Sl*mpl  +Sl*ml  -(1-Sl)*dpl -(1-Sl)*dl -dr*(1-max(Sr,R))  -dpr*(1-R) +mr*max(Sr,R) + mpr*R -anch_r_ft_edge*Sr +ar #AA(SR)
    if f3 > max(f1, f2):
        num_correct += 1
        print('CORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4))
    else:
        print('INCORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4))
        #anch_r_ft_edge += lr
        #Sr += lr

    print('\n(AAD)D))')
    num_tested += 1
    f1 = A*mpl +ml*A    -(1-A)*dpl -(1-A)*dl                    -dr                 -dpr                                          #(AA)DD
    f2 =        +ml*A   -dpl        -dl*(1-A)   +mr*D +mpr*D    -dr*(1-D)          -dpr*(1-D)                                     #A(AD)D
    f3 =                -dpl        -dl         +mr*D +mpr*D    -dr*(1-D)          -dpr*(1-D)          -anch_r_ft_edge*D   +ar       #AA(DD)
    if f2 > max(f1, f3):
        num_correct += 1
        print('CORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4))
    else:
        print('INCORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4))

    print('\nUU(S)ND)D)')
    num_tested += 1
    f1 =               -dpl         -dl       -dpr        -dr                           -dep_anch_left_stem #(UU)SNDD
    f2 =               -dpl         -dl      -dpr*(1-Sr) -dr*(1-D)  +D*mr +Sr*mpr                           #U(US)NDD
    f3 = ml*Sl +mpl*Sl -dpl*(1-Sl) -dl*(1-Sl) -dpr        -dr*(1-D) +D*mr                -anch_r_ft_edge*Sr #UU(SN)DD
    f4 = ml*Sl         -dpl         -dl*(1-Sl) -dpr*(1-D) -dr*(1-D) +D*mr +D*mpr                            #UUS(ND)D
    f5 = ml*Sl         -dpl        -dl*(1-Sl) -dpr*(1-D)  -dr*(1-D) +D*mr +D*mpr   +ar    -anch_r_ft_edge*D #UUSN(DD)

    if f4 > max(f1, f2, f3, f5):
        num_correct += 1
        print('CORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4), round(f4, 4), round(f5, 4))
    else:
        print('INCORRECT')
        #Sr += lr
        print(round(f1, 4), round(f2, 4), round(f3, 4), round(f4, 4), round(f5, 4))

    print('\n(AN(S)D)D)')
    num_tested += 1
    f1 = A*mpl +A*ml -(1-A)*dpl    -(1-A)*dl   -dr       -dpr                         #(AN)SDD
    f2 =       +Sl*ml      -dpl    -(1-Sl)*dl  -dr*(1-D) -dpr*(1-Sr) +Sr*mpr + D*mr  #A(NS)DD
    f3 = Sl*mpl +Sl*ml -(1-Sl)*dpl -(1-Sl)*dl -dr*(1-D) -dpr*(1-D)  +D*mpr  +D*mr  -anch_r_ft_edge*Sr  #AN(SD)D
    f4 =        +Sl*ml -dpl        -(1-Sl)*dl  -dr*(1-D) -dpr*(1-D)  +D*mpr +D*mr +ar -anch_r_ft_edge*D #ANS(DD)
    print(round(f1, 4), round(f2, 4), round(f3, 4), round(f4, 4))
    if f3 > max(f1, f2, f4):
        num_correct += 1
        print('CORRECT')
    else:
        print('INCORRECT')


    print('\n(AA(S)ND)D)')
    num_tested += 1
    f1 = A*mpl  +A*ml -(1-A)*dpl -(1-A)*dl     -dr         -dpr #(AA)SNDD
    f2 =         A*ml        -dpl   -dl*(1-A)  -dr*(1-D)   -dpr*(1-Sr) +mr*D +mpr*Sr #A(AS)NDD
    f3 = Sl*mpl +Sl*ml  -(1-Sl)*dpl  -(1-Sl)*dl -dr*(1-D)  -dpr      +mr*D             -anch_r_ft_edge*Sr #AA(SN)DD
    f4 =        +Sl*ml       -dpl   -(1-Sl)*dl -dr*(1-D)   -dpr*(1-D) +mr*D  +mpr*D       #AAS(ND)D
    f5 =        +Sl*ml       -dpl   -(1-Sl)*dl -dr*(1-D)   -dpr*(1-D) +mr*D  +mpr*D +ar -anch_r_ft_edge*D #AASN(DD)  
    if f4 > max(f1, f2, f3, f5):
        num_correct += 1
        print('CORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4), round(f4, 4), round(f5, 4))
    else:
        print('INCORRECT')
        print(round(f1, 4), round(f2, 4), round(f3, 4), round(f4, 4), round(f5, 4))
        #anch_r_ft_edge += lr
        #Sr += lr


    if num_correct == num_tested:
        print('\nALL CORRECT')
        break

print('\n\n')
for param, value in [
    ('A', A),('mpl', mpl),('dpl', dpl),('ml', ml),('dl', dl),('ar', ar),('dpr', dpr),('dr', dr),('mpr', mpr),('mr', mr),('Sl', Sl),('Sr', Sr),('u', u),('dep_anch_left_stem', dep_anch_left_stem),('anch_r_ft_edge', anch_r_ft_edge),('R', R),('D', D)]:
    print(param, value)
