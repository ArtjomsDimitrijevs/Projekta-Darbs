# Movie Finder Projekta darbs
## Projekta Apraksts
Šis Python projekts ir izstrādāts, lai ļautu lietotājam iegūt informāciju par filmām vai seriāliem, izmantojot Open Movie Database (OMDb) API. Projekts izmanto Tkinter bibliotēku, lai piedāvātu lietotājam draudzīgu saskarni, kur var ievadīt filmas nosaukumu un saņemt detalizētu informāciju par to.
## Projekta galvenie uzdevumi ir:

**Iegūt Informāciju Par Filmu**: Lietotājs ievada filmas nosaukumu, un programma izmanto OMDb API, lai iegūtu nosaukumu, izlaišanas gadu, ilgumu, žanru, sižetu un reitingu.  
**Atvērt Treileri IMDb**: Lietotājs var atvērt filmas treileri tieši no IMDb, izmantojot Selenium bibliotēku.  
**Saglabāt Informāciju Excel Dokumentā**: Projekts ļauj saglabāt filmu informāciju Excel dokumentā, lai lietotājs varētu sekmīgi uzglabāt skatītās filmas.  
## Izmantotās Python Bibliotēkas
**customtkinter**: Pielāgota Tkinter bibliotēka, kas nodrošina modernu saskarni un dizainu.  
**tkinter.messagebox**: Tkinter iebūvētā bibliotēka, izmantojama paziņojumu logiem.  
**selenium**: Bibliotēka pārlūkprogrammas darbības automatizācijai treilera atvēršanai IMDb.  
**requests**: Izmantots, lai veiktu HTTP pieprasījumus OMDb API.  
**openpyxl**: Bibliotēka darbam ar Excel failiem, izmantota, lai saglabātu filmu informāciju.  
**os**: Bibliotēka darbam ar operētājsistēmu, izmantota, lai pārbaudītu vai izveidotu Excel failu.  

## Programmas Lietošana
**Ievadīt Filmas Nosaukumu**: Ievadīt pilno filmas nosaukumu angļu valodā(Piem. Star Wars episode I, Green book, migration, Harry Potter and the Order of the Phoenix utt.).  
**Noklikšķināt uz "Find"**: Noklikšķināt uz pogas "Find", lai iegūtu informāciju par filmu.  
**Parādīt Informāciju un Opcijas**: Parādīsies informācija par filmu, un būs opcijas atvērt treileri vai saglabāt informāciju Excel dokumentā.  
**Atvērt Treileri IMDb**: Opcija atver treileri IMDb vietnē, lietojot pārlūkprogrammu.  
**Saglabāt Excel Dokumentā**: Opcija saglabāt iegūto informāciju Excel dokumentā "movies.xlsx".  
**Paziņojumi par Kļūdām**: Ja filma netiek atrasta, parādīsies kļūdas paziņojums.

## Darbība
Lai izmantotu šo programmu, ievadiet filmas nosaukumu angļu valodā un nospiediet "Find". Pēc tam parādīsies informācija par filmu. Jūs varat atvērt treileri IMDb vai saglabāt informāciju Excel dokumentā, izmantojot atbilstošās pogas. Paziņojumi par kļūdām parādīsies, ja filma netiek atrasta vai ir problēmas ar datu saglabāšanu. Treilera atvēršanai un datu saglabāšanai nepieciešams interneta pieslēgums.
