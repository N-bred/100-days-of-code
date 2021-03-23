const getDaysInMonth = (month, year) =>
  new Array(31)
    .fill('')
    .map((v, i) => new Date(year, month - 1, i + 1))
    .filter((v) => v.getMonth() === month - 1)
const fmtDate = (date) => date.toISOString().split('T')[0]

function getFullYearDates() {
  const date = new Date()
  const dates = []
  for (let m = 1; m <= 12; ++m) {
    const monthDates = getDaysInMonth(m, date.getFullYear())

    for (let d of monthDates) {
      dates.push(fmtDate(d))
    }
  }

  return dates
}

module.exports = getFullYearDates
