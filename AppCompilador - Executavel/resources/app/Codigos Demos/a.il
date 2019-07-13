.assembly extern mscorlib {}
.assembly _codigo_objeto{}
.module   _codigo_objeto.exe

.class public _UNICA {
.method static public void _principal() {
     .entrypoint
     .locals(int64 lado, int64 area)
     call string [mscorlib]System.Console::ReadLine()
     call int64 [mscorlib]System.Int64::Parse(string)
     stloc lado
     ldc.i8 0
     conv.r8
     conv.i8
     stloc area
     label1:
     ldloc lado
     conv.r8
     ldc.i8 0
     conv.r8
     cgt
     brfalse label2
     ldloc lado
     conv.r8
     ldloc lado
     conv.r8
     mul
     conv.i8
     stloc area
     label2:
     ldloc area
     conv.r8
     conv.i8
     call void [mscorlib]System.Console::Write(int64)
     ret
     }
}