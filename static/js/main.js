document.addEventListener(
    "DOMContentLoaded",
    () => {

        /*
        ==========================
        SIDEBAR
        ==========================
        */

        const sidebar =
            document.getElementById(
                "sidebar"
            );

        const toggle =
            document.getElementById(
                "sidebarToggle"
            );

        const content =
            document.querySelector(
                ".main-content"
            );

        if (
            sidebar &&
            toggle
        ) {

            function initializeSidebar() {

                if (
                    window.innerWidth <= 768
                ) {

                    sidebar.classList.remove(
                        "collapsed"
                    );

                    content?.classList.add(
                        "expanded"
                    );

                }

                else if (
                    window.innerWidth <= 1100
                ) {

                    sidebar.classList.add(
                        "collapsed"
                    );

                    content?.classList.add(
                        "expanded"
                    );

                }

                else {

                    sidebar.classList.remove(
                        "collapsed"
                    );

                    content?.classList.remove(
                        "expanded"
                    );

                }

            }

            initializeSidebar();

            window.addEventListener(
                "resize",
                initializeSidebar
            );

            toggle.addEventListener(
                "click",
                () => {

                    if (
                        window.innerWidth <= 768
                    ) {

                        sidebar.classList.toggle(
                            "mobile-open"
                        );

                    }

                    else {

                        sidebar.classList.toggle(
                            "collapsed"
                        );

                        content?.classList.toggle(
                            "expanded"
                        );

                    }

                }
            );

        }

        /*
        ==========================
        EXPENSE PIE CHART
        ==========================
        */

        const expensePieCanvas =
            document.getElementById(
                "expensePieChart"
            );

        if (expensePieCanvas) {

            new Chart(
                expensePieCanvas,
                {
                    type: "pie",

                    data: {

                        labels: JSON.parse(
                            expensePieCanvas.dataset.labels
                        ),

                        datasets: [
                            {
                                data: JSON.parse(
                                    expensePieCanvas.dataset.values
                                )
                            }
                        ]
                    },

                    options: {
                        responsive: true,
                        maintainAspectRatio: false
                    }

                }
            );

        }

        const analyticsPie =
            document.getElementById(
                "analyticsPieChart"
            );

        if (analyticsPie) {

            new Chart(
                analyticsPie,
                {
                    type: "pie",

                    data: {

                        labels: JSON.parse(
                            analyticsPie.dataset.labels
                        ),

                        datasets: [
                            {
                                data: JSON.parse(
                                    analyticsPie.dataset.values
                                )
                            }
                        ]
                    }
                }
            );
        }

        const analyticsTrend =
            document.getElementById(
                "analyticsTrendChart"
            );

        if (analyticsTrend) {

            new Chart(
                analyticsTrend,
                {
                    type: "line",

                    data: {

                        labels: JSON.parse(
                            analyticsTrend.dataset.labels
                        ),

                        datasets: [
                            {
                                label:
                                    "Expenses",

                                data: JSON.parse(
                                    analyticsTrend.dataset.values
                                )
                            }
                        ]
                    }
                }
            );
        }

        /*
        ==========================
        INCOME VS EXPENSES
        ==========================
        */

        const incomeExpenseCanvas =
            document.getElementById(
                "incomeExpenseChart"
            );

        if (incomeExpenseCanvas) {

            new Chart(
                incomeExpenseCanvas,
                {
                    type: "bar",

                    data: {

                        labels: JSON.parse(
                            incomeExpenseCanvas.dataset.labels
                        ),

                        datasets: [
                            {
                                label:
                                    "Amount",

                                data: JSON.parse(
                                    incomeExpenseCanvas.dataset.values
                                )
                            }
                        ]
                    },

                    options: {
                        responsive: true,
                        maintainAspectRatio: false
                    }

                }
            );

        }

        /*
        ==========================
        MONTHLY EXPENSE TREND
        ==========================
        */

        const expenseTrendCanvas =
            document.getElementById(
                "expenseTrendChart"
            );

        if (expenseTrendCanvas) {

            new Chart(
                expenseTrendCanvas,
                {
                    type: "line",

                    data: {

                        labels: JSON.parse(
                            expenseTrendCanvas.dataset.labels
                        ),

                        datasets: [
                            {
                                label:
                                    "Monthly Expenses",

                                data: JSON.parse(
                                    expenseTrendCanvas.dataset.values
                                ),

                                fill: true,

                                tension: 0.4,

                                borderWidth: 3
                            }
                        ]
                    },

                    options: {

                        responsive: true,

                        maintainAspectRatio: false,

                        plugins: {

                            legend: {
                                display: true
                            }

                        },

                        scales: {

                            y: {
                                beginAtZero: true
                            }

                        }

                    }

                }
            );

        }

    }
);