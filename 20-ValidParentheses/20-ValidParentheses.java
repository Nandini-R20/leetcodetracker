// Last updated: 8/11/2026, 12:27:09 PM
 class Solution {
    public boolean isValid(String s) {
   char[] stack = new char[s.length()];
   int top = -1;

  for (int i = 0; i < s.length(); i++) {
char c = s.charAt(i);


 if (c == '(' || c == '{' || c == '[') {
 if (top == s.length() - 1) {
              
 return false;
 }
   stack[++top] = c;
 } else {
                
   if (top == -1) {
  return false; 
 }
char last = stack[top--];

 if (!isPair(last, c)) {
  return false;
  }
   }
    }
 
  return top == -1;
    }

    private boolean isPair(char last, char c) {
        return (last == '(' && c == ')') ||
               (last == '{' && c == '}') ||
               (last == '[' && c == ']');
    }
} 