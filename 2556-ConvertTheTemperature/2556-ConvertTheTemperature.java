// Last updated: 8/11/2026, 12:20:44 PM
class Solution {
    public double[] convertTemperature(double celsius) {
        double Kelvin=celsius + 273.15;
        double Farenheit=(celsius * 1.80) + 32.00;
        double[] temp=new double[2];
        temp[0]=Kelvin;
        temp[1]=Farenheit;
        return temp;

    }
}