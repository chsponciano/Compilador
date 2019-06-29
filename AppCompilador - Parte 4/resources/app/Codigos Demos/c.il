.assembly extern mscorlib {}
.assembly _codigo_objeto{}
.module   _codigo_objeto.exe

.class public _UNICA {
.method static public void _principal() {
     .entrypoint
     .locals(int64 valor)
     call string [mscorlib]System.Console::ReadLine()
     call int64 [mscorlib]System.Int64::Parse(string)
     stloc valor
     label1:
     ldloc valor
     conv.r8
     ldc.i8 0
     conv.r8
     clt
     brfalse label2
     call string [mscorlib]System.Console::ReadLine()
     call int64 [mscorlib]System.Int64::Parse(string)
     stloc valor
     br label1
     label2:
     label3:
     ldloc valor
     conv.r8
     ldc.i8 0
     conv.r8
     ceq
     brtrue label4
     ldloc valor
     conv.r8
     conv.i8
     call void [mscorlib]System.Console::Write(int64)
     ldstr "\n"
     call void [mscorlib]System.Console::Write(string)
     ldloc valor
     conv.r8
     ldc.i8 1
     conv.r8
     sub
     conv.i8
     stloc valor
     br label3
     label4:
     ret
     }
}