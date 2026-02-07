/**
 * @typedef {Object} GSTResult
 * @property {number} originalAmount - The input amount before tax
 * @property {number} gstRate - The tax rate applied (in %)
 * @property {number} gstAmount - The calculated tax amount
 * @property {number} totalAmount - The final amount including tax
 */

/**
 * Calculates GST breakdown for a given amount and rate.
 * 
 * @param {number} amount - The base amount
 * @param {number} gstRate - The GST rate in percentage (e.g., 18 for 18%)
 * @returns {GSTResult} Detailed cost breakdown
 * @throws {Error} If inputs are negative or invalid
 */
function calculateGST(amount, gstRate) {
    if (typeof amount !== 'number' || typeof gstRate !== 'number') {
        throw new Error("Inputs must be numbers");
    }
    if (amount < 0 || gstRate < 0) {
        throw new Error("Amount and GST rate must be non-negative");
    }

    const gstAmount = (amount * gstRate) / 100;
    const totalAmount = amount + gstAmount;

    return {
        originalAmount: amount,
        gstRate: gstRate,
        gstAmount: parseFloat(gstAmount.toFixed(2)),
        totalAmount: parseFloat(totalAmount.toFixed(2))
    };
}

// --- Main Execution Block ---
try {
    console.log("--- GST Calculator Upgrade ---");
    
    // Example 1: Standard calc
    const result1 = calculateGST(1000, 18);
    console.log("Example 1 (1000 @ 18%):", result1);

    // Example 2: Small amount
    const result2 = calculateGST(150, 5);
    console.log("Example 2 (150 @ 5%):", result2);

    // Example 3: Error handling test (uncomment to test)
    // console.log(calculateGST(-100, 18)); 

} catch (error) {
    console.error("Error:", error.message);
}