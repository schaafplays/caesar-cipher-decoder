#Austin Schaaf
#Extra Credit 2
cipher = open("cipherText_2.txt", encoding="utf8")
cipherText = cipher.read()

def characterFrequency(cipher):
    '''
    This counts the total capital and lowercase letters in a string.
    Then compairs the 
    '''
    cifherText = cipher
    aC = cifherText.count("a")
    AC = cifherText.count("A")
    aaC = aC + AC
    bC = cifherText.count('b')
    BC = cifherText.count('B')
    bbC = bC + BC
    cC = cifherText.count("c")
    CC = cifherText.count('C')
    ccC = cC + CC
    dC = cifherText.count("d")
    DC = cifherText.count('D')
    ddC = dC + DC
    eC = cifherText.count('e')
    EC = cifherText.count('E')
    eeC = eC + EC
    fC = cifherText.count("f")
    FC = cifherText.count('F')
    ffC = fC + FC
    gC = cifherText.count("g")
    GC = cifherText.count('G')
    ggC = gC + GC
    hC = cifherText.count('h')
    HC = cifherText.count('H')
    hhC = hC + HC
    iC = cifherText.count("i")
    IC = cifherText.count('I')
    iiC = iC + IC
    jC = cifherText.count("j")
    JC = cifherText.count('J')
    jjC = jC + JC
    kC = cifherText.count('k')
    KC = cifherText.count('K')
    kkC = kC + KC
    lC = cifherText.count("l")
    LC = cifherText.count('L')
    llC = lC + LC
    mC = cifherText.count("m")
    MC = cifherText.count('M')
    mmC = mC + MC
    nC = cifherText.count('n')
    NC = cifherText.count('N')
    nnC = nC + NC
    oC = cifherText.count("o")
    OC = cifherText.count('O')
    ooC = oC + OC
    pC = cifherText.count("p")
    PC = cifherText.count('P')
    ppC = pC + PC
    qC = cifherText.count('q')
    QC = cifherText.count('Q')
    qqC = qC + QC
    rC = cifherText.count("r")
    RC = cifherText.count('R')
    rrC = rC + RC
    sC = cifherText.count("s")
    SC = cifherText.count('S')
    ssC = sC + SC
    tC = cifherText.count('t')
    TC = cifherText.count('T')
    ttC = tC + TC
    uC = cifherText.count("u")
    UC = cifherText.count('U')
    uuC = uC + UC
    vC = cifherText.count("v")
    VC = cifherText.count('V')
    vvC = vC + VC
    wC = cifherText.count('w')
    WC = cifherText.count('W')
    wwC = wC + WC
    xC = cifherText.count("x")
    XC = cifherText.count('X')
    xxC = xC + XC
    yC = cifherText.count("y")
    YC = cifherText.count('Y')
    yyC = yC + YC
    zC = cifherText.count('z')
    ZC = cifherText.count('Z')
    zzC = zC + ZC
    withoutWhite = cifherText.replace(' ','')
    withoutWhite = withoutWhite.replace('\n', '')
    withoutWhite = withoutWhite.replace(',', '')
    withoutWhite = withoutWhite.replace('-','')
    withoutWhite = withoutWhite.replace('.','')
    withoutWhite = withoutWhite.replace('(','')
    withoutWhite = withoutWhite.replace(')','')
    withoutWhite = withoutWhite.replace(';','')
    withoutWhite = withoutWhite.replace('"', '')
    withoutWhite = withoutWhite.replace("'",'')
    withoutWhite = withoutWhite.replace("!",'')
    withoutWhite = withoutWhite.replace('1','')
    withoutWhite = withoutWhite.replace('2','')
    withoutWhite = withoutWhite.replace('3','')
    withoutWhite = withoutWhite.replace('4','')
    withoutWhite = withoutWhite.replace('5','')
    withoutWhite = withoutWhite.replace('6','')
    withoutWhite = withoutWhite.replace('7','')
    withoutWhite = withoutWhite.replace('8','')
    withoutWhite = withoutWhite.replace('9','')
    withoutWhite = withoutWhite.replace('0','')
    cipherLen = len(withoutWhite)
    aF = (aaC / cipherLen) * 100
    bF = (bbC / cipherLen) * 100
    cF = (ccC / cipherLen) * 100
    dF = (ddC / cipherLen) * 100
    eF = (eeC / cipherLen) * 100
    fF = (ffC / cipherLen) * 100
    gF = (ggC / cipherLen) * 100
    hF = (hhC / cipherLen) * 100
    iF = (iiC / cipherLen) * 100
    jF = (jjC / cipherLen) * 100
    kF = (kkC / cipherLen) * 100
    lF = (llC / cipherLen) * 100
    mF = (mmC / cipherLen) * 100
    nF = (nnC / cipherLen) * 100
    oF = (ooC / cipherLen) * 100
    pF = (ppC / cipherLen) * 100
    qF = (qqC / cipherLen) * 100
    rF = (rrC / cipherLen) * 100
    sF = (ssC / cipherLen) * 100
    tF = (ttC / cipherLen) * 100
    uF = (uuC / cipherLen) * 100
    vF = (vvC / cipherLen) * 100
    wF = (wwC / cipherLen) * 100
    xF = (xxC / cipherLen) * 100
    yF = (yyC / cipherLen) * 100
    zF = (zzC / cipherLen) * 100
    totalF = aF + bF + cF + dF + eF + fF + gF + hF + iF + jF + kF + lF + mF + nF + oF + pF + qF + rF + sF + tF + uF + vF + wF + xF + yF + zF
    frequencyList = [aF,bF,cF,dF,eF,fF,gF,hF,iF,jF,kF,lF,mF,nF,oF,pF,qF,rF,sF,tF,uF,vF,wF,xF,yF]
    return frequencyList
def findShift(lists):
    frequencyList = lists
    findE = max(frequencyList)
    indexE = frequencyList.index(findE)
    shift = indexE - 4
    print("Shift: ",shift)
    return shift
def solveCipher(text,shift):
    cifer = text.lower()
    decoded = []
    test = ''
    #print(cifer)
    abc = "abcz"
    for i in cifer:
        code = ord(i) - shift
        if i.isalpha():
            if code > ord('z'):
                code = code - (ord('z') + 1 - ord('a'))
            if code < ord('a'):
                code = code + 26
            decoded.append(chr(code))
        else:
            decoded.append(i)
    test = test.join(decoded)
    return test   
    
frequencyList = characterFrequency(cipherText)
shift = findShift(frequencyList)
solved = solveCipher(cipherText,shift)
print(solved)
