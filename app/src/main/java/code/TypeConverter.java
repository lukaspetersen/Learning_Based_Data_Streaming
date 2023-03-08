package code;

import java.math.BigInteger;

public class TypeConverter {

    public static BigInteger stringToBigInteger(String str) {
        return new BigInteger(str.getBytes());
    }

    public static String bigIntegerToString(BigInteger bigInt) {
        return new String(bigInt.toByteArray());
    }

}
