
flag = "?" 

X = {
    string = flag,
    len = #flag,
    counter = 3
}

s = "1357924680ACEBDF1357924680ACEBDF1357924680ACEBDF1357924680ACEBDF13579246ACEBDF135792"
Y = {
    string = s,
    len = #s,
    counter = 3
}

M = {}
M.__add = function(a, b)
    l1 = a.len
    l2 = b.len
    l = math.min(l1, l2)
    Z = {
        string = "",
        len = l,
        counter = 3
    }
    c = 1
    while c~=l+1 do
        Z.string = Z.string .. string.char((string.byte(a.string,c) ~ string.byte(b.string,c)))
        c = c+1
    end
    return Z
end


M.__unm = function(x)
    c = 1
    res = ""
    Z = {
        string = "",
        len = x.len,
        counter = 3
    }
    while c~=x.len+1 do
        res = res..string.char(math.fmod(x.string:byte(c)+0x23, 255))
        c = c+1
    end
    Z.string = res
    return Z
end

setmetatable(X, M)
X = -X
setmetatable(X, M)
t = X+Y

c = 1
result = ""
while c~=t.len+1 do
    result = result..string.format("%02X ", t.string:byte(c))
    c = c+1
end

print(result)