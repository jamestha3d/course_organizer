
export const dateToDay = (dateTime) => {
    const year = dateTime.getFullYear();
    const month = ('0' + (dateTime.getMonth() + 1)).slice(-2); // Months are zero-indexed
    const day = ('0' + dateTime.getDate()).slice(-2);
    
    // Create a date string in YYYY-MM-DD format
    const dateString = `${year}-${month}-${day}`;

    return dateString
}
