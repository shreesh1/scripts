import idc
import idaapi
import idautils
import codecs

ea = idc.get_screen_ea()
func = idaapi.get_func(ea)
start = idc.get_func_attr(ea, FUNCATTR_START)
end = idc.get_func_attr(ea, FUNCATTR_END)
curr_addr = start
while curr_addr <= end:
        if(not(idc.print_operand(curr_addr,1).find('offset'))):
                fa = curr_addr
                print(hex(curr_addr),idc.generate_disasm_line(curr_addr,0))
                a = idc.get_operand_value(curr_addr,1)
                print(hex(idaapi.get_byte(int(a))))
                for i in range(4):
                	curr_addr = idc.next_head(curr_addr,end)
                k = idc.get_operand_value(curr_addr,1)
                lo = ""
                for i in range(a,a+k+1):
                        lo+=bytes.fromhex(hex(255*int(idaapi.get_byte(int(i))))[4:]).decode()
                idc.set_cmt(fa,lo,0)
                curr_addr = idc.next_head(curr_addr,end)
        else:
                curr_addr = idc.next_head(curr_addr,end)
