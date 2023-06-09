#### Вариант 1 - готовый датасет

- предсказание банкротства тайваньских компаний - 
https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction

- 96 столбцов с интерпретируемыми обозначениями,
- около 7 тыс. строк

#### Вариант 2 - собрать что-то похожее из открытых источников

- единый реестр субъектов малого и среднего предпринимательства, около 20 Гб файлов xml
https://www.nalog.gov.ru/opendata/7707329152-rsmp/

примерная структура:

	<Документ ИдДок="d984367e-51f2-4e8c-b853-572a4cef850a" ДатаСост="10.03.2023" ДатаВклМСП="01.08.2016" ВидСубМСП="1" КатСубМСП="1" ПризНовМСП="2" СведСоцПред="2" ССЧР="1">
	        <ОргВклМСП НаимОрг="ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ &quot;...&quot;" НаимОргСокр="ООО &quot;...&quot;" ИННЮЛ="" ОГРН=""/>
	        <СведМН КодРегион="">
	            <Регион Тип="ОБЛАСТЬ" Наим=""/>
	            <Район Тип="РАЙОН" Наим=""/>
	            <Город Тип="ГОРОД" Наим=""/>
	        </СведМН>
	        <СвОКВЭД>
	            <СвОКВЭДОсн КодОКВЭД="32.9" НаимОКВЭД="Производство изделий, не включенных в другие группировки" ВерсОКВЭД="2014"/>
	            <СвОКВЭДДоп КодОКВЭД="47.5" НаимОКВЭД="Торговля розничная прочими бытовыми изделиями в специализированных магазинах" ВерсОКВЭД="2014"/>
	            ...
	        </СвОКВЭД>
	    </Документ>

где:

	- ПризНовМСП - признак вновь возданного МСП, 
	- ССЧР - среднее число работников, 
	- СвОКВЭДОсн - осн. вид деятельности, 
	- СвОКВЭДДоп - произвольное число дополнительных типов деятельности
	- Плюсом может содержать сведения о лицензиях, некоторых контрактах и т.д.

- Сведения об уплаченных организацией в календарном году налогах - файлы xml.


		<Документ ИдДок="" ДатаДок="" ДатаСост="">
		    <СведНП НаимОрг="" ИННЮЛ=""/>
		    <СвУплСумНал НаимНалог="НЕНАЛОГОВЫЕ ДОХОДЫ, администрируемые налоговыми органами" СумУплНал=""/>
		    ...
		</Документ>


- Сведения о среднесписочной численности работников организации (но они же есть и в едином реестре), xml
https://www.nalog.gov.ru/opendata/7707329152-sshr2019/

- Сведения о суммах доходов и расходов по данным бухгалтерской (финансовой) отчетности организации за год, предшествующий году размещения таких сведений на сайте ФНС России - только доход и расход, xml
https://www.nalog.gov.ru/opendata/7707329152-revexp/

- Сведения о суммах недоимки и задолженности по пеням и штрафам - xml
https://www.nalog.gov.ru/opendata/7707329152-debtam/


		<Документ ИдДок="" ДатаДок="" ДатаСост="">
		    <СведНП НаимОрг="" ИННЮЛ=""/>
		    <СведНедоим НаимНалог="Страховые взносы на обязательное медицинское страхование работающего населения, зачисляемые в бюджет Федерального фонда обязательного медицинского страхования" СумНедНалог="" СумПени="" СумШтраф="" ОбщСумНедоим=""/>
		    ...
		</Документ>


- Единый реестр субъектов малого и среднего предпринимательства – получателей поддержки
https://www.nalog.gov.ru/opendata/7707329152-rsmppp/

- реестр дисквалифицированных лиц 
https://www.nalog.gov.ru/opendata/7707329152-registerdisqualified/

- физ лица, являющиеся руководителями нескольких юр.лиц (ИНН, ФИО, число юр. лиц), csv
 https://www.nalog.gov.ru/opendata/7707329152-massleaders/

- физ лица, являющиеся учредителями (участниками) нескольких юр.лиц - csv
https://www.nalog.gov.ru/opendata/7707329152-massfounders/

+ куча справочников 

- бухгалтерский баланс и отчёт о финансовых результатах собранные вместе я не нашла, но на сайте https://bo.nalog.ru есть собранная информация о бизнесах (для каждого - на отдельной страничке, поиск по ИНН даёт однозначный результат)

https://bo.nalog.ru/organizations-card/11101704

Адрес формируется с использованием id а не ИНН или другого понятного идентификатора - т.е. чуть больше переходов.

Часть информации пересекается с той, которую можно достать из xls-файлов.

- можно дополнительно обогатить данные - есть множество справочников, агрегированная информация по регионам и т.д.

https://mintrud.gov.ru/opendata
https://rosstat.gov.ru/opendata/7708234640-showdatabest

- примерная структура датасета

	- уникальный id
	- средн. числ. работников
	- код осн.деятельности (м.б. + число дополнительных видов деятельности)
	- регион
	- является ли вновь созданным
	- уставной капитал, активы и т.д.
	- данные бухгалтерского баланса
	- данные из отчёта о фин. результатах

	если будет время:
	- задолженности по налогам, дисквалификация и т.д.
	- доп. информация (безработица в регионе, уровень цен, соц-дем характеристики по регионам)

- пока смутно представляю себе, что брать в качестве цели:

	- кажется, недостаточно информации, чтобы посчитать Cost of Debt (общая сумма процентов за год/общая сумма всех долгов * (1 - налоговая ставка))
	- совокупный фин. результат периода (либо его изменение от предыдущего периода %)
    - баланс или кредиторские задолженности по краткосрочным/долгосрочным обязательствам (либо их рост/падение %)
    - что-либо ещё

- надо будет определиться, какие предприятия брать (так как для разных - разная отчётность и соответственно, разные доступные данные).
