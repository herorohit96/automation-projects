/**
 * Financial Tracker - Production Script 🏭
 * Purpose: GST calculate karna aur transactions ko log karna.
 * 
 * Usage: node financial_tracker.js
 */

const fs = require('fs');

/**
 * Calculates GST breakdown.
 * (Logic same as before - Amount aur Rate se Tax nikalta hai)
 * @param {number} amount 
 * @param {number} gstRate 
 */
function calculateGST(amount, gstRate) {
    if (amount < 0 || gstRate < 0) throw new Error("Values must be positive");
    const gstAmount = (amount * gstRate) / 100;
    return {
        amount,
        gstRate,
        gstAmount: parseFloat(gstAmount.toFixed(2)),
        total: parseFloat((amount + gstAmount).toFixed(2))
    };
}

// Simulated Database (Abhi ke liye memory mein save kar rahe hain)
const transactions = [];

function addTransaction(description, amount, gstRate) {
    console.log(`Processing: ${description}...`);
    try {
        const result = calculateGST(amount, gstRate); // Same logic use kar rahe hain
        const record = {
            id: transactions.length + 1,
            desc: description,
            ...result,
            date: new Date().toISOString()
        };
        transactions.push(record);
        console.log("✅ Transaction Saved:", record);
    } catch (e) {
        console.error("❌ Error (Galti hui):", e.message);
    }
}

// --- Execution Block (Kaam Shuru) ---
console.log("--- MY FINANCIAL TRACKER (FACTORY) ---");

// Test Cases (Kuch entries daal ke dekhte hain)
addTransaction("Freelance Project A", 50000, 18);
addTransaction("Software License", 12000, 18);
addTransaction("Office Supplies", 1500, 5);

// --- Monthly Summary (Mahine ka Hisaab) ---
console.log("\n--- Monthly Summary (Hisaab Kitab) ---");

// Total Revenue (Kul Aamdani)
const totalRevenue = transactions.reduce((sum, t) => sum + t.total, 0);

// Total GST Collected (Sarkar ka hissa)
const totalGST = transactions.reduce((sum, t) => sum + t.gstAmount, 0);

// Total Earnings without Tax (Apni kamaai)
const netEarnings = totalRevenue - totalGST;

console.log(`📊 Total Transactions: ${transactions.length}`);
console.log(`💰 Total Revenue (with GST): ₹${totalRevenue.toFixed(2)}`);
console.log(`🏛️  Total GST Collected:     ₹${totalGST.toFixed(2)}`);
console.log(`✅ Net Earnings (Profit):   ₹${netEarnings.toFixed(2)}`);

console.log("\nSystem Status: All systems stable. 🚀");
