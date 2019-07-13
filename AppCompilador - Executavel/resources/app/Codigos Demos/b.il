.assembly extern mscorlib {}
.assembly _codigo_objeto{}
.module   _codigo_objeto.exe

.class public _UNICA {
.method static public void _principal() {
     .entrypoint
     .locals(float64 valor)
     call string [mscorlib]System.Console::ReadLine()
     call float64 [mscorlib]System.Double::Parse(string)
     stloc valor
     label1:
     ldloc valor
     ldc.r8 0.0
     cgt
     brfalse label2
     ldstr "maior"
     call void [mscorlib]System.Console::Write(string)
     br label3
     label2:
     ldstr "menor ou igual"
     call void [mscorlib]System.Console::Write(string)
     label3:
     ret
     }
}