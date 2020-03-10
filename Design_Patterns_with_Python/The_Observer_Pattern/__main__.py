# https://app.pluralsight.com/course-player?clipId=5bd7ae1e-0892-478a-a626-49b2884194cd
# before observer pattern
from before_observer import KPI_Data

# Report on current KPI values
for kpi in KPI_Data:
	if kpi.name == "open":
		print("Current open tickets: %s" % kpi.value)
	
	elif kpi.name == "new":
		print("New tickets in last hour: %s" % kpi.value)

	elif kpi.name == "closed":
		print("Tickets closed in last hour: %s" % kpi.value)



# observer pattern
from kpis import KPIs
from currentkpis import CurrentKPIs
from forecastkpis import ForecastkpisKPIs


# Report on current KPI values
kpis = KPIs()
currentKPIs = CurrentKPIs(kpis)
forecastKPIs = ForecastkpisKPIs(kpis)

kpis.set_kpis(25, 10, 5)
kpis.set_kpis(100, 50, 30)
kpis.set_kpis(50, 10, 20)

print("\n***Detaching the currentKPIs observer.***\n\n")
kpis.detach(currentKPIs)
kpis.set_kpis(150, 110, 120)