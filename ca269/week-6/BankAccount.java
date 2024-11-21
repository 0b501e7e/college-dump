public class BankAccount {
    double balance;
    public BankAccount() {
        balance = 100.00;
    }

    public void withdraw(double amount) {
        balance -= amount;
    }
    public void deposit(double amount) {
        balance += amount;
    }
    public String toString() {
        return "The balance is " + balance;
    }
}